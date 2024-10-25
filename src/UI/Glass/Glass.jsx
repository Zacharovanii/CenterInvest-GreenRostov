import cl from "./Glass.module.css"

function Glass({ children }) {
	return (
		<div className={cl.glass} >
			{children}
		</div>
	)
}

export default Glass
