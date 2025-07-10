export function ViagemMensagem({ local, viagensFiltradas }) {
    return (
        <div
            style={viagensFiltradas.length === 1 ? { display: 'flex', flexDirection: 'row', justifyContent: 'space-around', alignItems: 'center', marginTop: '3rem' } : null}
        >
            <div>
                {local && viagensFiltradas.length <= 0 && (
                    <div style={{ marginTop: '3rem' }}>
                        <h3 className='bus-txt-local'>{"Não encontramos nenhuma viagem para o destino desejado."}</h3>
                    </div>
                )}
            </div>
        </div>
    );
}
