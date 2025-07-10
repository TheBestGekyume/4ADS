import { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './perfil.scss';

export function Perfil() {
    const navigate = useNavigate();
    const [userData, setUserData] = useState({
        nome: '',
        email: '',
        senha: '',
        confirmarSenha: ''
    });
    const [originalData, setOriginalData] = useState({});
    const [isEditing, setIsEditing] = useState(false);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const [showDeleteModal, setShowDeleteModal] = useState(false);

    useEffect(() => {
        const userId = window.sessionStorage.getItem('id_usuario');
        if (!userId) {
            navigate('/login');
            return;
        }

        carregarDadosUsuario();
    }, [navigate]);

    const carregarDadosUsuario = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/usuarios/${window.sessionStorage.getItem('id_usuario')}`);
            const user = response.data;
            setUserData({
                nome: user.nome,
                email: user.email,
                senha: '',
                confirmarSenha: ''
            });
            setOriginalData({
                nome: user.nome,
                email: user.email
            });
        } catch (err) {
            setError('Erro ao carregar dados do usuário');
            console.error(err);
        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setUserData(prev => ({ ...prev, [name]: value }));
        if (error) setError('');
    };

    const handleEditar = () => {
        setIsEditing(true);
        setError('');
        setSuccess('');
    };

    const handleCancelar = () => {
        setIsEditing(false);
        setUserData(prev => ({
            ...prev,
            nome: originalData.nome,
            email: originalData.email,
            senha: '',
            confirmarSenha: ''
        }));
    };

    const handleSalvar = async (e) => {
        e.preventDefault();

        if (!userData.nome || !userData.email) {
            setError('Nome e e-mail são obrigatórios');
            return;
        }

        if (userData.senha && userData.senha !== userData.confirmarSenha) {
            setError('As senhas não coincidem');
            return;
        }

        try {
            const payload = {
                id_usuario: window.sessionStorage.getItem('id_usuario'),
                nome: userData.nome,
                email: userData.email,
                ...(userData.senha && { senha: userData.senha })
            };

            await axios.put('http://localhost:5000/usuarios/editar', payload);

            setSuccess('Dados atualizados com sucesso!');
            setIsEditing(false);
            window.sessionStorage.setItem('nome', userData.nome);

            setOriginalData({
                nome: userData.nome,
                email: userData.email
            });

            setUserData(prev => ({ ...prev, senha: '', confirmarSenha: '' }));

        } catch (err) {
            setError(err.response?.data?.error || 'Erro ao atualizar dados');
            console.error(err);
        }
    };

    const handleExcluirConta = async () => {
        try {
            await axios.delete('http://localhost:5000/usuarios/excluir', {
                data: { id_usuario: window.sessionStorage.getItem('id_usuario') }
            });

            window.sessionStorage.clear();
            navigate('/login', { replace: true });
            window.location.reload();

        } catch (err) {
            setError('Erro ao excluir conta');
            console.error(err);
        } finally {
            setShowDeleteModal(false);
        }
    };

    return (
        <div className="perfil-container">
            <h2>Meu Perfil</h2>

            {error && <div className="alert alert-danger">{error}</div>}
            {success && <div className="alert alert-success">{success}</div>}

            <form onSubmit={handleSalvar}>
                <div className="mb-3">
                    <label htmlFor="nome" className="form-label">Nome</label>
                    <input
                        type="text"
                        className="form-control"
                        id="nome"
                        name="nome"
                        value={userData.nome}
                        onChange={handleInputChange}
                        disabled={!isEditing}
                    />
                </div>

                <div className="mb-3">
                    <label htmlFor="email" className="form-label">E-mail</label>
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        name="email"
                        value={userData.email}
                        onChange={handleInputChange}
                        disabled={!isEditing}
                    />
                </div>

                {isEditing && (
                    <>
                        <div className="mb-3">
                            <label htmlFor="senha" className="form-label">Nova Senha (deixe em branco para não alterar)</label>
                            <input
                                type="password"
                                className="form-control"
                                id="senha"
                                name="senha"
                                value={userData.senha}
                                onChange={handleInputChange}
                                placeholder="Digite sua nova senha"
                            />
                        </div>

                        <div className="mb-3">
                            <label htmlFor="confirmarSenha" className="form-label">Confirmar Nova Senha</label>
                            <input
                                type="password"
                                className="form-control"
                                id="confirmarSenha"
                                name="confirmarSenha"
                                value={userData.confirmarSenha}
                                onChange={handleInputChange}
                                placeholder="Confirme sua nova senha"
                            />
                        </div>

                        <div className="button-group">
                            <button type="submit" className="btn btn-success">
                                Salvar Alterações
                            </button>
                            <button type="button" className="btn btn-secondary" onClick={handleCancelar}>
                                Cancelar
                            </button>
                        </div>
                    </>
                )}
            </form>

            {!isEditing && (
                <div className="button-group w-50 mx-auto">
                    <button type="button" className="btn btn-primary" onClick={handleEditar}>
                        Editar Perfil
                    </button>
                    <button
                        type="button"
                        className="btn btn-danger"
                        onClick={() => setShowDeleteModal(true)}
                    >
                        Excluir Conta
                    </button>
                </div>
            )}

            {showDeleteModal && (
                <div className="modal-overlay">
                    <div className="modal-content">
                        <h3>Confirmar Exclusão</h3>
                        <p>Tem certeza que deseja excluir sua conta? Esta ação não pode ser desfeita.</p>
                        <div className="modal-buttons">
                            <button
                                className="btn btn-danger"
                                onClick={handleExcluirConta}
                            >
                                Confirmar Exclusão
                            </button>
                            <button
                                className="btn btn-secondary"
                                onClick={() => setShowDeleteModal(false)}
                            >
                                Cancelar
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
