import { useEffect, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import onibus from "../../assets/onibus.png";
import disponivel from "../../assets/assentoDisponivel.png";
import indisponivel from "../../assets/assentoIndisponivel.png";
import selecionado from "../../assets/assentoSelecionado.png";
import { LoadConfirm } from '../../components/LoadConfirm';
import './escolherAssento.scss';
import { ModalError } from '../../components/ModalError/ModalError';

export function EscolherAssento() {
    const [viagem, setViagem] = useState(null);
    const [assentosSelecionados, setAssentosSelecionados] = useState([]);
    const [searchParams] = useSearchParams();
    const navigate = useNavigate();
    const viagemId = searchParams.get('id');
    const usuarioId = window.sessionStorage.getItem("id_usuario");
    const [confirmarPedido, setConfirmarPedido] = useState(null);
    const [totalPassagem, setTotalPassagem] = useState(0);
    const [modalError, setModalError] = useState(false);

    const formatarDataPTBR = (dataISO) => {
        const [year, month, day] = dataISO.split('-');
        return `${day}/${month}/${year}`;
    };

    useEffect(() => {
        const token = window.sessionStorage.getItem("token");
        if (!token) {
            navigate('/login');
            return;
        }

        if (!viagemId) {
            console.error("ID da viagem não encontrado.");
            return;
        }

        axios.get(`http://localhost:5000/viagens/${viagemId}`)
            .then((response) => {
                const viagemData = response.data;
                if (viagemData) {
                    setViagem({
                        id: viagemData.id_viagem,
                        assentos: viagemData.assentos,
                        preco: viagemData.preco,
                        data_de_partida: viagemData.data_de_partida,
                        horario_de_partida: viagemData.horario_de_partida
                    });
                } else {
                    console.error("Viagem não encontrada.");
                }
            })
            .catch((error) => {
                console.error('Erro ao carregar viagens:', error);
                setModalError('Erro ao carregar detalhes da viagem');
            });
    }, [viagemId, navigate]);

    useEffect(() => {
        if (viagem) {
            setTotalPassagem(Math.ceil(assentosSelecionados.length) * viagem.preco);
        }
    }, [assentosSelecionados, viagem]);

    const toggleSelecionarAssento = (nro_assento) => {
        setAssentosSelecionados((prev) =>
            prev.includes(nro_assento)
                ? prev.filter((assento) => assento !== nro_assento)
                : [...prev, nro_assento]
        );
    };

    const handleCompra = async () => {
        const assentosIndisponiveis = assentosSelecionados.map((nro_assento) => ({ nro_assento }));
        const objetoCompra = {
            id_viagem: viagem.id,
            usuario_id: usuarioId,
            assentos_indisponiveis: assentosIndisponiveis
        };

        console.log("JSON para requisição:", JSON.stringify(objetoCompra));

        try {
            const response = await axios.put("http://localhost:5000/viagens/comprar-assento", objetoCompra);
            console.log(response.data);
            setConfirmarPedido(true);
        } catch (error) {
            console.log(error.response);
        }
    };

    const getAssentoImage = (assento) => {
        if (assentosSelecionados.includes(assento.nro_assento)) {
            return selecionado;
        }
        return assento.disponivel ? disponivel : indisponivel;
    };

    if (!viagem) {
        return <p>Carregando...</p>;
    }

    const fileiraA = viagem.assentos.filter(assento => assento.nro_assento.startsWith('A'));
    const fileiraB = viagem.assentos.filter(assento => assento.nro_assento.startsWith('B'));
    const closeModalError = () => {
        setModalError(false);
    }


    console.log(viagem)
    return (
        <div className="container-selecao-assentos" style={{ height: '100vh' }}>
            <div style={{ width: '80%', zIndex: '10', display: "flex", justifyContent: 'flex-end', position: 'fixed', marginTop: '1rem' }}>
                {modalError && <ModalError msg={modalError} closeModalError={closeModalError} />}
            </div>
            <div style={{ width: '100%', display: "flex", justifyContent: 'space-between', marginTop: "2rem" }}>
                <svg style={{ cursor: 'pointer', marginLeft: '2rem' }} onClick={() => navigate(-1)} xmlns="http://www.w3.org/2000/svg" width="30" height="30" className="bi bi-arrow-left-circle-fill" viewBox="0 0 16 16">
                    <path fill="#FFB803" d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0m3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z" />
                </svg>
                <div>
                    {!confirmarPedido && <h3 style={{ marginRight: "2rem" }} className='text-white'><strong>Selecionar Assentos</strong></h3>}
                    {!confirmarPedido && <p style={{ marginRight: "2rem" }} className='text-white'><strong>Hora de Partida:</strong> {viagem.horario_de_partida}</p>}
                    {!confirmarPedido && <p style={{ marginRight: "2rem" }} className='text-white'><strong>Data de Partida:</strong> {formatarDataPTBR(viagem.data_de_partida)}</p>}
                </div>
            </div>

            {!confirmarPedido && (
                <div className="onibus-container d-flex justify-content-center flex-wrap">
                    <img src={onibus} alt="Ônibus" className="onibus-imagem position-absolute" />
                    <div className='assentos-container d-flex flex-column'>
                        <div style={{ display: "flex", flexDirection: "row" }}>
                            {fileiraA.map((assento, index) => (
                                <div style={{ margin: '0', padding: '0' }} key={index}>
                                    <p style={{ margin: '0', padding: '0' }}>{assento.nro_assento}</p>
                                    <img
                                        src={getAssentoImage(assento)}
                                        alt={`Assento ${assento.nro_assento}`}
                                        className="assento-imagem fileira-A rounded"
                                        onClick={() => assento.disponivel && toggleSelecionarAssento(assento.nro_assento)}
                                    />
                                </div>
                            ))}
                        </div>
                        <div style={{ display: "flex", flexDirection: "row" }}>
                            {fileiraB.map((assento, index) => (
                                <div className='p-0 m-0' key={index}>
                                    <p className='p-0 m-0'>{assento.nro_assento}</p>
                                    <img
                                        src={getAssentoImage(assento)}
                                        alt={`Assento ${assento.nro_assento}`}
                                        className="assento-imagem fileira-B rounded"
                                        onClick={() => { assento.disponivel && toggleSelecionarAssento(assento.nro_assento) }}

                                    />
                                </div>
                            ))}
                        </div>
                    </div>
                    <section style={{ width: "100%", marginTop: '10rem', display: 'flex', justifyContent: "space-around", alignItems: 'center' }}>
                        <div className='container-tipo-assento'>
                            <figure className='d-flex align-items-end text-white fw-bolder me-3 gap-2'>
                                <img className="assento-imagem fileira-B" src={disponivel} style={{ width: "60px" }} />
                                <p>Disponível</p>
                            </figure>

                            <figure className='d-flex align-items-end text-white fw-bolder me-3 gap-2'>
                                <img className="assento-imagem fileira-B" src={indisponivel} style={{ width: "60px", borderRadius: '8px' }} />
                                <p>Indisponível</p>
                            </figure>

                            <figure className='d-flex align-items-end text-white fw-bolder me-3 gap-2'>
                                <img className="assento-imagem fileira-B" src={selecionado} style={{ width: "60px", borderRadius: '8px' }} />
                                <p>Selecionado</p>
                            </figure>
                        </div>
                        <button className='buscar-viagem' onClick={() => {
                            if (assentosSelecionados.length > 0) {
                                handleCompra();
                            } else {
                                setModalError('Selecione um ou mais assentos para comprar.')
                            }
                        }}>
                            Comprar
                        </button>
                    </section>
                </div>
            )}
            {confirmarPedido && (
                <div>
                    <h1 className='text-white'>Passagem comprada com sucesso!</h1>
                    <LoadConfirm />
                </div>
            )}
            {!confirmarPedido && <div className="total-container">
                <h3>Total a pagar: R$ {totalPassagem.toFixed(2)}</h3>
            </div>}
        </div>
    );
}
