import { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
//rotas
import { Login } from './pages/Login/Login.jsx';
import { Home } from './pages/Home/Home.jsx';
import { About } from './pages/About/About.jsx';
import { Passagens } from './pages/Passagens/Passagens.jsx';
import { EscolherAssento } from './pages/EscolherAssento/EscolherAssento.jsx';
import { MinhasViagens } from './pages/MinhasViagens/MinhasViagens.jsx';
import { Perfil } from './pages/Perfil/Perfil.jsx';
//components
import { Footer } from './components/Footer/Footer.jsx';
import { NavBar } from './components/NavBar/NavBar.jsx';
import './app.scss';
import { ItemNavProvider } from './context/itemNavContext.jsx';

export function App() {
  const [token, setToken] = useState(window.sessionStorage.getItem('token'));

  return (
    <ItemNavProvider>
      <Router>
        <div className="d-flex bg-black h-100">
          {token && <NavBar setToken={setToken} />}
          <main className='container mb-5'>
            <Routes>
              <Route path="/login" element={<Login setToken={setToken} />} />
              <Route path="/" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/passagens" element={<Passagens />} />
              <Route path="/escolherAssento" element={<EscolherAssento />} />
              <Route path="/minhasViagens" element={<MinhasViagens />} />
              <Route path="/perfil" element={<Perfil />} />
            </Routes>
          </main>
        </div>
        {token && <Footer />}
      </Router>
    </ItemNavProvider>
  );
}
