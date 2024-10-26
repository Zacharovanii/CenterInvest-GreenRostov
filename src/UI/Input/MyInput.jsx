import React from 'react'

function MyInput(props) {
	return (
		<div>
			<label htmlFor={props.info.id}></label>
			<input type={props.type} id={props.info.id} />
		</div>
	)
}

export default MyInput
