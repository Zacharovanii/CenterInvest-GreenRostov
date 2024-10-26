import React, { useContext } from 'react'
import MyInput from '../UI/input/MyInput'
import MyButton from '../UI/button/MyButton'
import { AuthContext } from '../context'

function Login() {
	const { isAuth, setIsAuth } = useContext(AuthContext)
	const login = event => {
		event.preventDefault()
		setIsAuth(true)
		localStorage.setItem('auth', 'true')
	}

	return (
		<div className="glass">
			<h1 className="loginH1" >Login</h1>
			<form onSubmit={login}>
				<MyInput className="loginInput" type="text" placeholder='Enter login' />
				<MyInput className="loginInput" type="password" placeholder='Enter password' />
				<MyInput className="loginInput" type="tel" placeholder='Enter number' />
				<MyButton>Enter</MyButton>
			</form>
		</div>
	)
}

export default Login
