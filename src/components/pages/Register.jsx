import React, { useContext, useState } from 'react'
import MyInput from '../UI/input/MyInput'
import MyButton from '../UI/button/MyButton'
import { AuthContext } from '../context'
import PostService from '../API/PostService'

function Login() {
	const { isAuth, setIsAuth } = useContext(AuthContext)

	const [FIO, setFIO] = useState({ name: '', lastname: '', surname: '' })
	const [email, setEmail] = useState('')
	const [pass, setPass] = useState('')
	const [phone, setPhone] = useState('')

	const register = event => {
		event.preventDefault()
		setIsAuth(true)
		localStorage.setItem('auth', 'true')
		PostService.registerUser(
			{
				name: FIO.name,
				lastname: FIO.lastname,
				surname: FIO.surname,
				phone_number: phone,
				password: pass,
				email: email,
				is_active: true,
				is_superuser: false,
				is_verified: false,
				level: 0,
				points: 0,
				achievements: [
					0
				],
				events: [
					0
				],
				role_id: 0,
				registered_at: "2024-10-27 08:20:41.727"
			}
		)
	}

	return (
		<div className="glass">
			<h1 className="loginH1" >Register</h1>
			<form onSubmit={register}>
				<MyInput
					className="loginInput"
					type="text"
					placeholder='Name'
					value={FIO.name}
					onChange={e => setFIO({ ...FIO, name: e.target.value })}
				/>
				<MyInput
					className="loginInput"
					type="text"
					placeholder='Lastname'
					value={FIO.lastname}
					onChange={e => setFIO({ ...FIO, lastname: e.target.value })}
				/>
				<MyInput
					className="loginInput"
					type="text"
					placeholder='Surname'
					value={FIO.surname}
					onChange={e => setFIO({ ...FIO, surname: e.target.value })}
				/>
				<MyInput
					className="loginInput"
					type="email"
					placeholder='Email'
					value={email}
					onChange={e => setEmail(e.target.vale)}
				/>
				<MyInput
					className="loginInput"
					type="password"
					placeholder='Password'
					value={pass}
					onChange={e => setPass(e.target.vale)}
				/>
				<MyInput
					className="loginInput"
					type="tel"
					placeholder='Enter number'
					value={phone}
					onChange={e => setPhone(e.target.vale)}
				/>
				<MyButton>Enter</MyButton>
			</form>
		</div>
	)
}

export default Login
