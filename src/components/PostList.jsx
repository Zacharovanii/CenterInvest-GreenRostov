import React from 'react'
import PostItem from './PostItem'
import { TransitionGroup, CSSTransition } from 'react-transition-group'
import UserSidebar from './UserSidebar'

function PostList({ posts, title, remove, modalFunc }) {

	if (!posts.length) {
		return (
			<h1 style={{ textAlign: 'center' }} >
				Post are not founded!
			</h1>
		)
	}
	return (
		<div className="post-list">
			<UserSidebar modalFunc={modalFunc} />
			<div className="post_glass">
				{title}
			</div>
			<TransitionGroup>
				{posts.map((post, index) =>
					<CSSTransition
						key={post.id}
						timeout={500}
						classNames='post'
					>
						<PostItem remove={remove} number={index + 1} post={post} />
					</CSSTransition>
				)}
			</TransitionGroup>
		</div>
	)
}

export default PostList
