import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import "./about.scss"
import maletaIcon from '../../assets/maletaIcon.png'
import missaoIcon from '../../assets/missaoIcon.png'


export function About() {
    const token = window.sessionStorage.getItem("token");

    const navigate = useNavigate();
    useEffect(() => {
        if (!token) {
            navigate('/login');
        } else {
            window.sessionStorage.setItem("itemNav", 1);
        }
    }, [token, navigate]);

    if (token) {
        return (
            <div id='about' className='text-white'>
                <section className='my-5 ps-5'>
                    <div className="row gap-4">
                        <div className='col-4 text-center'>
                            <h2>QUEM SOMOS</h2>
                            <p>A Viação Calango é uma renomada empresa de transporte interestadual que tem como objetivo proporcionar aos seus passageiros uma experiência de viagem segura, confortável e confiável. Com uma trajetória sólida e uma equipe dedicada, somos referência no setor e nos orgulhamos de oferecer serviços de alta qualidade.</p>
                        </div>

                        <div className='col-3'></div>

                        <div className='col'>
                            <img src={maletaIcon} alt="" />
                        </div>
                    </div>
                </section>

                <section className='mt-5 '>
                    <div className="row gap-4">
                        <div className='col-1'></div>

                        <div className='col'>
                            <img src={missaoIcon} alt="" />
                        </div>

                        <div className='col-3'></div>

                        <div className='col-4 text-center'>
                            <h2>NOSSA MISSÃO</h2>
                            <p>A Viação Calango é uma empresa de ônibus interestadual dedicada a fornecer serviços de transporte confiáveis e seguros, conectando pessoas e comunidades em todo o país. Nossa missão é oferecer viagens de qualidade, pontuais e acessíveis, priorizando a segurança e a satisfação dos passageiros. Estamos comprometidos em ser uma empresa de referência no setor, contribuindo para a mobilidade e o desenvolvimento do país.</p>
                        </div>

                        <div className='col'></div>
                    </div>
                </section>

            </div>
        );
    }
}
