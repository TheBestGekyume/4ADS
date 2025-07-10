import React, { useState, useEffect } from 'react';
import './modalAddViagem.scss';
import axios from 'axios';

export function ModalAddViagem({ isOpen, onClose, refreshViagens, idViagem }) {
  const [formData, setFormData] = useState({
    origem: '',
    destino: '',
    horario_de_partida: '',
    data_de_partida: '',
    preco: '',
    assentos: '',
    imgUrl: ''
  });

  const [error, setError] = useState('');
  useEffect(() => {
    if (idViagem) {
      const fetchViagem = async () => {
        try {
          const response = await axios.get(`http://localhost:5000/viagens/${idViagem}`);
          if (response.data) {
            setFormData(response.data);
            console.log('Dados da viagem carregados com sucesso:', response.data);
          }
        } catch (error) {
          console.error('Erro ao carregar os dados da viagem:', error);
        }
      };
      fetchViagem();
    } else {
      setFormData({
        origem: '',
        destino: '',
        horario_de_partida: '',
        data_de_partida: '',
        preco: '',
        assentos: '',
        imgUrl: ''
      });
    }
  }, [idViagem]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.assentos % 2 !== 0 && !idViagem) {
      setError('O número de assentos deve ser par!');
      return;
    }

    setError('');

    try {
      if (idViagem) {
        const response = await axios.put('http://localhost:5000/viagens/editar', {
          id_viagem: idViagem,
          ...formData
        });
        alert(response.data.success || response.data.error);
      } else {
        const response = await axios.post('http://localhost:5000/viagens/criar', formData);
        alert(response.data.success || response.data.error);
      }

      onClose();
      refreshViagens();
    } catch (error) {
      console.error('Erro ao salvar a viagem:', error);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay vw-100">
      <div className="modal-content w-50 p-3 pb-4 px-5">
        <button className="close-button px-3 m-2 fs-2 rounded-4" onClick={onClose}>X</button>
        <h2 className='text-white'>{idViagem ? 'Editar Viagem' : 'Adicionar Nova Viagem'}</h2>

        {error && <p className="alert alert-danger p-2 mt-2 d-flex mx-auto">{error}</p>}

        <form onSubmit={handleSubmit} className='mt-3'>
          <section className='border-0 d-flex flex-column align-items-center gap-3'>
            <div className='d-flex gap-2 align-items-end'>
              <label className='fs-5 pe-3'>Origem:</label>
              <input type="text" name="origem" value={formData.origem} onChange={handleChange} required />
            </div>
            <div className='d-flex gap-2 align-items-end justify-content-start'>
              <label className='fs-5 pe-3'>Destino:</label>
              <input type="text" name="destino" value={formData.destino} onChange={handleChange} required />
            </div>
            <div className='d-flex gap-2 align-items-end justify-content-start'>
              <label className='fs-5 pe-3'>Horário de Partida:</label>
              <input type="time" name="horario_de_partida" value={formData.horario_de_partida} onChange={handleChange} required />
            </div>
            <div className='d-flex gap-2 align-items-end justify-content-start'>
              <label className='fs-5 pe-3'>Data de Partida:</label>
              <input type="date" name="data_de_partida" value={formData.data_de_partida} onChange={handleChange} required />
            </div>
            <div className='d-flex gap-2 align-items-end justify-content-start'>
              <label className='fs-5 pe-3'>Preço:</label>
              <input type="number" name="preco" value={formData.preco} onChange={handleChange} required />
            </div>
            {!idViagem && (
              <>
                <div className='d-flex gap-2 align-items-end justify-content-start'>
                  <label className='fs-5 pe-3'>Número de Assentos:</label>
                  <input type="number" name="assentos" value={formData.assentos} onChange={handleChange} required />
                </div>
                <div className='d-flex gap-2 align-items-end justify-content-start'>
                  <label className='fs-5 pe-3'>URL da Imagem:</label>
                  <input type="text" name="imgUrl" value={formData.imgUrl} onChange={handleChange} required />
                </div>
              </>
            )}

          </section>
          <button type="submit" className='mt-2'>{idViagem ? 'Salvar Alterações' : 'Adicionar Viagem'}</button>
        </form>
      </div>
    </div>
  );
}
