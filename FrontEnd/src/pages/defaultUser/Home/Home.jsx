import React, { useContext, useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Card } from '../../../components/Card/Card';
import { ModalAddViagem } from '../../../components/ModalAddViagem/ModalAddViagem';
import "./home.scss";
import axios from 'axios';
import { ItemNavContext } from '../../../context/itemNavContext';

export function Home() {
  const token = window.sessionStorage.getItem("token");
  const typeUser = Number(window.sessionStorage.getItem("typeUser"));
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [viagens, setViagens] = useState([]);
  const { setItemNavdOption} = useContext(ItemNavContext);

  const navigate = useNavigate();

  useEffect(() => {
    if (!token) {
      navigate('/login');
    } else {
      window.sessionStorage.setItem("itemNav", 0);
    }
  }, [token, navigate]);

  const openModal = () => setIsModalOpen(true);
  const closeModal = () => setIsModalOpen(false);

  const refreshViagens = () => {
    axios.get('http://localhost:5000/viagens')
      .then((response) => {
        setViagens(response.data || []);
      })
      .catch((error) => {
        console.error("Erro ao buscar as viagens:", error);
      });
  };

  useEffect(() => {
    refreshViagens();
  }, []);

  if (token) {
    return (
      <div id='home' className='text-white text-center pt-5'>
        {typeUser === 0 &&
          <Link to="/passagens" onClick={() => {window.sessionStorage.setItem("itemNav", 2); setItemNavdOption(2)}}>
            <button className='btn btn-lg text-white mb-5' type='button'>
              <h3>COMPRE ANTECIPADO E GANHE 10% DE DESCONTO</h3>
            </button>
          </Link>
        }

        {typeUser === 1 &&
          <button className='btn btn-lg text-white mb-5' type='button' onClick={openModal}>
            Cadastrar viagem
          </button>
        }

        <section className='mx-5 rounded-4'>
          <Card viagens={viagens} />
        </section>

        <ModalAddViagem isOpen={isModalOpen} onClose={closeModal} refreshViagens={refreshViagens} />
      </div>
    );
  }
}
