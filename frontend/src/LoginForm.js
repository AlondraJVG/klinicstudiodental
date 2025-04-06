// src/LoginForm.js
import { useState } from 'react';
import { login } from './services/api';

function LoginForm() {
  const [correo, setCorreo] = useState('');
  const [contrasena, setContrasena] = useState('');
  const [mensaje, setMensaje] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await login(correo, contrasena);
    setMensaje(data.mensaje);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={correo} onChange={e => setCorreo(e.target.value)} placeholder="Correo" />
      <input type="password" value={contrasena} onChange={e => setContrasena(e.target.value)} placeholder="Contraseña" />
      <button type="submit">Iniciar Sesión</button>
      <p>{mensaje}</p>
    </form>
  );
}
