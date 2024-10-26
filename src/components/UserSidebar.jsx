import React from 'react'

function UserSidebar() {
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
			<button className="profile-button" >Go to profile</button>
		</div>
	)
}

export default UserSidebar
