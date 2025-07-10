import { useState } from 'react';
import './destinoUser.scss';
import origem from "../../assets/origem.png";
import date from "../../assets/date.png";
import destino from "../../assets/destino.png";
import { ModalError } from '../ModalError/ModalError';

export function DestinoUser({ setLocal, local }) {
    const [modalError, setModalError] = useState(false);
    const [origemDestinoUser, setOrigemDestinoUser] = useState({
        origem: '',
        destino: '',
        ida: '',
        volta: ''
    });

    const eventOnChange = (e) => {
        const { name, value } = e.target;
        setOrigemDestinoUser((prevState) => ({
            ...prevState,
            [name]: value
        }));
    };

    const dataBrasil = (dateString) => {
        if (!dateString) return "";
        const [year, month, day] = dateString.split('-');
        return `${day}/${month}/${year}`;
    };

    const validarOrigemDestino = (origem, destino) => {
        if (origem && destino) {
            return true;
        } else {
            setModalError("Um ou mais campos não foram preenchidos corretamente!");
        }
    }

    const closeModalError = () => {
        setModalError(false);
    }

    return (
        <div>
            <div style={{ width: '80%', zIndex: '10', display: "flex", justifyContent: 'flex-end', position: 'fixed', marginTop: '1rem' }}>
                {modalError && <ModalError msg={modalError} closeModalError={closeModalError}/>}
            </div>
            <section className='section-destinoUser'>
                <div>
                    <p>Origem</p>
                    <div className='container-input-dest'>
                        <img
                            className='img-origem-user'
                            src={origem}
                            alt='icone origem'
                        />
                        <input
                            type='text'
                            name='origem'
                            value={origemDestinoUser.origem}
                            onChange={eventOnChange}
                            placeholder='Origem'
                            autoFocus
                        />
                    </div>
                </div>

                <div>
                    <p>Destino</p>
                    <div className='container-input-dest'>
                        <img
                            className='img-destino-user'
                            src={destino}
                            alt='icone destino'
                        />
                        <input
                            type='text'
                            name='destino'
                            value={origemDestinoUser.destino}
                            onChange={eventOnChange}
                            placeholder='Destino'
                        />
                    </div>
                </div>

                <div>
                    <p>Ida</p>
                    <div className='container-input-dest'>
                        <img
                            className='date-destino-user'
                            src={date}
                            alt='icone data'
                            onClick={() => document.getElementById("ida").showPicker()}
                        />
                        <input
                            type='date'
                            id='ida'
                            name='ida'
                            value={origemDestinoUser.ida}
                            onChange={eventOnChange}
                            min={new Date().toISOString().split('T')[0]}
                            style={{ opacity: 0, position: 'absolute', pointerEvents: 'none' }}
                        />
                        <span className="data-display">{dataBrasil(origemDestinoUser.ida) || "dd/mm/aaaa"}</span>
                    </div>
                </div>

                <div>
                    <p>Volta</p>
                    <div className='container-input-dest'>
                        <img
                            className='date-destino-user'
                            src={date}
                            alt='icone data'
                            onClick={() => document.getElementById("volta").showPicker()}
                        />
                        <input
                            type='date'
                            id='volta'
                            name='volta'
                            value={origemDestinoUser.volta}
                            onChange={eventOnChange}
                            min={origemDestinoUser.ida || new Date().toISOString().split('T')[0]}
                            style={{ opacity: 0, position: 'absolute', pointerEvents: 'none' }}
                        />
                        <span className="data-display">{dataBrasil(origemDestinoUser.volta) || "dd/mm/aaaa"}</span>
                    </div>
                </div>
                <div style={{ display: "flex", alignItems: 'flex-end' }}>
                    <div style={{ display: 'flex', alignItems: 'flex-end' }}>
                        <button onClick={() => {
                            if (validarOrigemDestino(origemDestinoUser.origem, origemDestinoUser.destino)) {
                                setLocal(origemDestinoUser)
                            }
                        }} className='buscar-viagem'><span>Buscar viagem</span></button>
                    </div>
                </div>
            </section>
            {local && <svg style={{ cursor: 'pointer', marginTop: '2rem' }} onClick={() => setLocal(null)} xmlns="http://www.w3.org/2000/svg" width="30" height="30" className="bi bi-arrow-left-circle-fill" viewBox="0 0 16 16">
                <path fill="#FFB803" d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0m3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z" />
            </svg>}
        </div>
    );
}
