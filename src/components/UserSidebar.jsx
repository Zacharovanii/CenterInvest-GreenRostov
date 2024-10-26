import React, { useState } from 'react'
import MyModal from './UI/MyModal/MyModal'

function UserSidebar({ modalFunc }) {

	return (
		<div className="sidebar">
			<h1>Иван Иванов Иванович</h1>
			<div className='user-level' >
				<p>0</p>
				<div className='level' ></div>
			</div>
			<div className="user_info" >
				<p>My Posts: 1</p>
				<p>Status: 1</p>
				<p>C02: 1</p>
				<p>Phone Number: 1</p>
				<p>Register date: 1</p>
				<p><span>Email:</span> <span>1</span></p>
			</div>
			<button className="CO2-button" onClick={() => modalFunc(true)} >Count C02</button>
			<button className="profile-button" >Go to profile</button>
		</div>
	)
}

export default UserSidebar
