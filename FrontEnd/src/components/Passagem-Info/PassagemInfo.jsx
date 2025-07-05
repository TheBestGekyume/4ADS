import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import "./passagemInfo.scss";
import map from "../../assets/map.png";
import { Load } from '../Load';
import { ViagemMensagem } from '../ViagemMensagem/ViagemMensagem';
import { ModalAddViagem } from '../ModalAddViagem/ModalAddViagem';

export function PassagemInfo({ local }) {
    const [viagens, setViagens] = useState([]);
    const [erro, setErro] = useState(null);
    const navigate = useNavigate();
    const tipoUsuario = window.sessionStorage.getItem("typeUser");
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [idViagemSelecionada, setIdViagemSelecionada] = useState(null);

    const openModal = (idViagem = null) => {
        setIdViagemSelecionada(idViagem);
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIdViagemSelecionada(null);
        setIsModalOpen(false);
    };

    const refreshViagens = () => {
        axios.get('http://localhost/5000/viagens')
            .then((response) => {
                setViagens(response.data || []);
            })
            .catch((error) => {
                console.error("Erro ao buscar as viagens:", error);
            });
    };

    const deletarViagem = async (idViagem) => {
        const confirmDelete = window.confirm("Tem certeza que deseja excluir esta viagem?");
        if (!confirmDelete) return;

        try {
            const response = await axios.delete('http://localhost/5000/crudViagem/deletarViagem.php', {
                data: { id_viagem: idViagem }
            });

            if (response.data.status === "success") {
                alert(response.data.message);
                refreshViagens();
            } else {
                alert(response.data.message || "Erro ao deletar a viagem.");

            }
        } catch (error) {
            console.error("Erro ao deletar a viagem:", error);
            alert("Erro ao deletar a viagem. Tente novamente.");
        }
    };

    useEffect(() => {
        refreshViagens();
    }, []);

    if (erro) {
        return <p>{erro}</p>;
    }

    if (viagens.length === 0) {
        return (
            <div>
                <Load />
                <p>Carregando informações das viagens...</p>
            </div>
        );
    }

    const getCityName = (city) => {
        return city.split(" -")[0].trim();
    };

    const normalizeString = (str) => {
        return str
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, "")
            .toLowerCase();
    };

    const viagensFiltradas = local && local.origem && local.destino
        ? viagens.filter(
            (viagem) =>
                normalizeString(getCityName(viagem.origem)) === normalizeString(getCityName(local.origem)) &&
                normalizeString(getCityName(viagem.destino)) === normalizeString(getCityName(local.destino))
        )
        : viagens;

    const handleVerMais = (viagemId) => {
        navigate(`/escolherAssento?id=${viagemId}`);
    };

    return (
        <>
            <ViagemMensagem local={local} viagensFiltradas={viagensFiltradas} />

            {viagensFiltradas.map((viagem, index) => (
                <section key={index} className='container-passagem-info p-3' style={viagensFiltradas.length === 1 ? { width: '600px' } : {}}>
                    <div className="d-flex align-items-start">
                        <img className='map-passagem-info' src={map} alt="Mapa" />
                        <div>
                            <p>Origem: {viagem.origem}</p>
                            <p>Destino: {viagem.destino}</p>
                        </div>
                    </div>
                    <div className="d-flex align-items-center">
                        <p>A partir de <strong>R${parseFloat(viagem.preco).toFixed(2)}</strong></p>


                    </div>
                    {tipoUsuario === "0" && (
                        <button
                            onClick={() => handleVerMais(viagem.id_viagem)}
                            className='button-horarios-passagem-info'
                        >
                            Ver Mais
                        </button>
                    )}

                    {tipoUsuario === "1" && (
                        <div className="d-flex flex-column gap-2">
                            <button
                                className='btn bg-warning text-white'
                                type='button'
                                onClick={() => openModal(viagem.id_viagem)}
                            >
                                Editar
                            </button>
                            <button
                                className='btn bg-danger text-white'
                                type='button'
                                onClick={() => deletarViagem(viagem.id_viagem)}
                            >
                                Deletar
                            </button>
                        </div>
                    )}
                </section>
            ))}

            <ModalAddViagem
                isOpen={isModalOpen}
                onClose={closeModal}
                refreshViagens={refreshViagens}
                idViagem={idViagemSelecionada}
            />
        </>
    );
}
