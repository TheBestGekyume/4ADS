import 'bootstrap/dist/css/bootstrap.min.css';
import './card.scss';

export function Card({ viagens }) {
  const formatarDataPTBR = (dataISO) => {
    const [year, month, day] = dataISO.split('-');
    return `${day}/${month}/${year}`;
  };

  return (
    <div id="card" className="container px-3">
      <div className="row">
        {viagens.length > 0 ? (
          viagens.slice(0, 4).map((viagem, index) => (
            <div className="col-md-6 my-4" key={index}>
              <div className="card h-100 border- bg-transparent d-flex">
                <img
                  src={viagem.imgUrl}
                  className="card-img rounded-5 height-limit"
                  alt={`${viagem.origem} - ${viagem.destino}`}
                />
                <div className="card-body flex-grow-0 flex-fill bg-warning mt-3 rounded-5">
                  <h5 className="card-title text-white ">{viagem.origem} → {viagem.destino}</h5>
                  <p className="card-text fw-bolder">
                    Data: {formatarDataPTBR(viagem.data_de_partida)}<br />
                    Horário: {viagem.horario_de_partida}<br />
                    Preço: R$ {parseFloat(viagem.preco).toFixed(2)}
                  </p>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12 text-center">
            <p>Não há viagens disponíveis.</p>
          </div>
        )}
      </div>
    </div>
  );
}
