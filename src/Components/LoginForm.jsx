import { useState } from 'react'
import Glass from '../UI/Glass/Glass'
import "./LoginForm.module.css"

function LoginForm() {
	const [login, setLogin] = useState("")

	return (
		<Glass>
			<form action="" method="get">
				<div className="head">
					<h3>Войти</h3>
				</div>

				<div className="login-fields">
					<label htmlFor="login">Логин</label>
					<input type="text" id="login" />

				</div>
			</form>
		</Glass>
	)
}

export default LoginForm
