import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './styles.css';

const Signup = () => {
	const [username, setUsername] = useState('');
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [confirmPassword, setConfirmPassword] = useState('');
	const [error, setError] = useState('');

	const handleSignup = async (e) => {
		e.preventDefault();
		try {
			const response = await axios.post('http://localhost:8000/user/signup/', {
				username,
				email,
				password,
				confirm_password: confirmPassword,
			});
			// Handle successful signup (e.g., redirect to login)
			console.log(response.data);
		} catch (err) {
			setError(err.response.data.error || 'Signup failed');
		}
	};

	return (
		<div className="signup-container">
			<nav className="navbar">
				<ul>
					<li><Link to="/">Home</Link></li>
					<li><Link to="/login">Login</Link></li>
					<li><Link to="/about">About</Link></li>
				</ul>
			</nav>
			<h2>Signup</h2>
			<form onSubmit={handleSignup}>
				<input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" required />
				<input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
				<input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
				<input type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} placeholder="Confirm Password" required />
				<button type="submit">Signup</button>
				{error && <p className="error">{error}</p>}
			</form>
		</div>
	);
};

export default Signup;
