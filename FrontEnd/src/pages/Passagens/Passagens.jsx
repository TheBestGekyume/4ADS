import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { DestinoUser } from '../../components/Destino-usuario/DestinoUser.jsx';
import { PassagemInfo } from '../../components/Passagem-Info/PassagemInfo.jsx';
import "./passagens.scss";


export function Passagens() {

    const navigate = useNavigate();
    const token = window.sessionStorage.getItem("token");
    const [local, setLocal] = useState(null);

    useEffect(() => {
        if (!token) {
            navigate('/login');
        }
    }, [token, navigate]);

    if (token) {
        return (
            <div className='w-100 h-100 d-flex flex-column align-items-center mt-3 mb-5'>
                <div className='w-100 px-4'>
                    <DestinoUser setLocal={setLocal} local={local}/>
                </div>
                <section className='d-flex flex-wrap'>
                    <PassagemInfo  local={local}/>
                </section>
            </div>
        );
    }
}
