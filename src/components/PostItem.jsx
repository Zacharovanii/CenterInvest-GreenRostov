import React from "react";
import MyButton from "./UI/button/MyButton";
import { useHistory } from 'react-router-dom'

const PostItem = (props) => {
	const router = useHistory()
	return (
		<div className="post_glass">
			<div className="post__children">
				<strong>{props.post.id}. {props.post.title}</strong>
				<div>
					{props.post.body}
				</div>
			</div>
			<div className="post__btns">
				<button className="add_post" onClick={() => router.push(`/posts/${props.post.id}`)} >
					+
				</button>
			</div>
		</div>
	)
}

export default PostItem