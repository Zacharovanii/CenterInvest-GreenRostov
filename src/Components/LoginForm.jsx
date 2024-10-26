import { useState } from 'react'
import Glass from '../UI/Glass/Glass'
import "./LoginForm.module.css"

function LoginForm() {
	const [login, setLogin] = useState("")
	const [pass, setPassword] = useState("")

	function checkUser() {
		pass
	}

	return (
		<Glass>
			<form method="get">
				<div className="head">
					<h3>Авторизироваться</h3>
				</div>

				<div className="login-fields">
					<label htmlFor="login">Логин</label>
					<input
						type="text"
						id="login"
						onChange={e => setLogin(e.target.value)}
					/>
					<label htmlFor="password">Пароль</label>
					<input
						type="password"
						id="login"
						onChange={e => setPassword(e.target.value)}
					/>
				</div>
				<button
					type='submit'
					onClick={checkUser}
				>
					Войти
				</button>
			</form>
		</Glass>
	)
}

export default LoginForm
