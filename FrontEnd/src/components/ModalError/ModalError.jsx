import './modalError.scss';

export function ModalError({ msg, closeModalError }) {
    return (
        <div className='container-modal-error'>
            <p>{msg}</p>
            <p onClick={closeModalError} style={{cursor:'pointer'}}>X</p>
        </div>
    )
}
