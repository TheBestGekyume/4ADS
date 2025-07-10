import { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import "./login.scss";
import busIcon from '../../assets/busIcon.png';

export function Login({ setToken }) {
    const [userCredentials, setUserCredentials] = useState({
        email: '',
        senha: '',
        nome: '',
    });
    const [statusErros, setStatusErros] = useState(null);
    const [isRegistering, setIsRegistering] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        if (window.sessionStorage.getItem('token')) {
            navigate("/");
        }
    }, [navigate]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setUserCredentials(prev => ({ ...prev, [name]: value }));

        if ((name === 'senha' || name === 'confirmarSenha') && statusErros === "As senhas não coincidem") {
            setStatusErros(null);
        }
    };

    const logarUsuario = (e) => {
        e.preventDefault();

        axios.post('http://localhost:5000/autenticar', {
            email: userCredentials.email,
            senha: userCredentials.senha
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then((response) => {
                const { status, tipo, nome, id_usuario } = response.data;
                window.sessionStorage.setItem('token', status);
                window.sessionStorage.setItem('typeUser', tipo);
                window.sessionStorage.setItem('nome', nome);
                window.sessionStorage.setItem('id_usuario', id_usuario);
                setToken(status);
                navigate("/");
            })
            .catch((error) => {
                console.error("Erro no login:", error);
                setStatusErros(error.response?.data?.mensagem || "Erro de autenticação");
            });
    };

    const registrarUsuario = (e) => {
        e.preventDefault();

        // Validações
        if (!userCredentials.nome || !userCredentials.email || !userCredentials.senha || !userCredentials.confirmarSenha) {
            setStatusErros("Preencha todos os campos obrigatórios");
            return;
        }

        if (userCredentials.senha !== userCredentials.confirmarSenha) {
            setStatusErros("As senhas não coincidem");
            return;
        }

        const payload = {
            nome: userCredentials.nome,
            email: userCredentials.email,
            senha: userCredentials.senha
        };

        axios.post('http://localhost:5000/usuarios/criar', payload, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(() => {
                setStatusErros("Registro realizado com sucesso! Faça login.");
                setIsRegistering(false);
                setUserCredentials(prev => ({
                    ...prev,
                    senha: '',
                    confirmarSenha: ''
                }));
            })
            .catch((error) => {
                console.error("Erro no registro:", error);
                setStatusErros(error.response?.data?.error || "Erro ao registrar usuário");
            });
    };

    const toggleRegister = () => {
        setIsRegistering(!isRegistering);
        setStatusErros(null);
    };

    return (
        <div id='login'>
            {!window.sessionStorage.getItem('token') && (
                <>
                    <img src={busIcon} alt="viação calango" />

                    <div className='d-flex justify-content-center align-items-center flex-column pt-5'  
                        >
                        <form className='text-center py-3 px-4' onSubmit={isRegistering ? registrarUsuario : logarUsuario}>
                            <h1>{isRegistering ? 'Criar Conta' : 'Fazer Login'}</h1>

                            {isRegistering && (
                                <div className='d-flex flex-column text-start mb-3 mt-3'>
                                    <label className='fs-4' htmlFor="nome">Nome Completo</label>
                                    <input
                                        className='form-control mt-2'
                                        name='nome'
                                        type='text'
                                        placeholder="Seu nome"
                                        value={userCredentials.nome}
                                        onChange={handleInputChange}
                                    />
                                </div>
                            )}

                            <div className='d-flex flex-column text-start mb-3'>
                                <label className='fs-4' htmlFor="email">E-mail</label>
                                <input
                                    className='form-control mt-2'
                                    name='email'
                                    type='email'
                                    placeholder="Seu e-mail"
                                    value={userCredentials.email}
                                    onChange={handleInputChange}
                                />
                            </div>

                            <div className='d-flex flex-column text-start mb-3'>
                                <label className='fs-4' htmlFor="senha">Senha</label>
                                <input
                                    className='form-control mt-2'
                                    name='senha'
                                    type="password"
                                    placeholder="Sua senha"
                                    value={userCredentials.senha}
                                    onChange={handleInputChange}
                                />
                            </div>

                            {isRegistering && (
                                <div className='d-flex flex-column text-start mb-3'>
                                    <label className='fs-4' htmlFor="confirmarSenha">Confirmar Senha</label>
                                    <input
                                        className='form-control mt-2'
                                        name='confirmarSenha'
                                        type="password"
                                        placeholder="Confirme sua senha"
                                        value={userCredentials.confirmarSenha}
                                        onChange={handleInputChange}
                                    />
                                </div>
                            )}


                            <button type="submit" className='btn btn-lg w-100 text-black mt-4'>
                                {isRegistering ? 'Registrar' : 'Entrar'}
                            </button>

                            <a
                                className='mt-3 text-white text-decoration-none'
                                onClick={toggleRegister}
                            >

                                {isRegistering ? 'Já tem uma conta? Faça login' : 'Não tem uma conta? Registre-se'}

                            </a>
                        </form>

                        {statusErros && (
                            <div className={`alert ${statusErros.includes("sucesso") ? "alert-success" : "alert-danger"} mt-3`}>
                                {statusErros}
                            </div>
                        )}
                    </div>
                </>
            )}
        </div>
    );
}