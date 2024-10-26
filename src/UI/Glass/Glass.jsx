import cl from "./Glass.module.css"

function Glass({ children }) {
	return (
		<div
			// className="h-full w-full bg-gray-200 rounded-md bg-clip-padding backdrop-filter backdrop-blur-md bg-opacity-10 border border-gray-100" >
			className={cl.glass}
		>
			{children}
		</div>
	)
}

export default Glass
