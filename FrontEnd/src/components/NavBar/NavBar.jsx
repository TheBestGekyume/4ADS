import { useContext, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import "./navBar.scss";
import busIcon from "../../assets/busIcon.png";
import { IconPessoa } from '../IconPessoa';
import { ItemNavContext } from '../../context/itemNavContext';


export function NavBar({ setToken }) {
  const navigate = useNavigate();
  const [itemNav, setItemNav] = useState(Number(window.sessionStorage.getItem("itemNav")) || 0);
  const {itemNavOption} = useContext(ItemNavContext)
  const nomeUsuario = window.sessionStorage.getItem("nome");
  const tipoUsuario = window.sessionStorage.getItem("typeUser");

  const logoutUser = () => {
    window.sessionStorage.clear();
    setToken(null);
    navigate("/");
  };

  return (
    <nav>
      <figure className='figure ms-2'>
        <img src={busIcon} className='mx-auto d-block' alt="busIcon" />
      </figure>


      <div className='mb-5 pb-2 text-center'>
        <IconPessoa />
        <p className='mt-2'>{nomeUsuario}</p>
        {tipoUsuario === "1" && (
          <p>(admin)</p>
        )}
      </div>

      <ul className='p-0'>
        <li className={itemNav === 0 ? "styleLi" : "opacity-50"} >
          <Link onClick={() => { setItemNav(0); }} className='link-router-dom' to="/">Página inicial</Link>
        </li>
        <li className={itemNav === 1 ? "styleLi " : "opacity-50"} >
          <Link onClick={() => { setItemNav(1); }} className='link-router-dom' to="/about">Sobre</Link>
        </li>
        <li className={(itemNav === 2 || itemNavOption === 2) ? "styleLi" : "opacity-50"} >
          <Link onClick={() => { setItemNav(2); }} className='link-router-dom' to="/passagens">Passagens</Link>
        </li>
        {tipoUsuario === "0" && (
          <li className={itemNav === 3 ? "styleLi" : "opacity-50"} >
            <Link onClick={() => { setItemNav(3); }} className='link-router-dom' to="/minhasViagens">Minhas Viagens</Link>
          </li>
        )}
        <li onClick={logoutUser} className='opacity-50'>
          Sair
        </li>
      </ul>
    </nav>
  );
}
