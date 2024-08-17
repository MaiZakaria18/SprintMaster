import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './styles.css';

const Login = () => {
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [error, setError] = useState('');

	const handleLogin = async (e) => {
		e.preventDefault();
		try {
			const response = await axios.post('http://localhost:8000/user/login/', { email, password });
			// Handle successful login (e.g., store tokens, redirect)
			console.log(response.data);
		} catch (err) {
			setError(err.response.data.error || 'Login failed');
		}
	};

	return (
		<div className="login-container">
			<nav className="navbar">
				<ul>
					<li><Link to="/">Home</Link></li>
					<li><Link to="/signup">Register</Link></li>
					<li><Link to="/about">About</Link></li>
				</ul>
			</nav>
			<h2>Login</h2>
			<form onSubmit={handleLogin}>
				<input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
				<input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
				<button type="submit">Login</button>
				{error && <p className="error">{error}</p>}
			</form>
		</div>
	);
};

export default Login;
