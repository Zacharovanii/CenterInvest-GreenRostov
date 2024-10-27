import axios from "axios"

export default class PostService {
	static async getAll(limit = 10, page = 1) {
		const response = await axios.get('https://jsonplaceholder.typicode.com/posts',
			{
				params: {
					_limit: limit,
					_page: page
				}
			}
		)
		return response
	}

	static async getById(id) {
		const response = await axios.get(`https://jsonplaceholder.typicode.com/posts/${id}`)
		return response
	}

	static async getCommentsByPostId(id) {
		const response = await axios.get(`https://jsonplaceholder.typicode.com/posts/${id}/comments`)
		return response
	}

	static async registerUser(params) {
		const response = await axios.post("http://127.0.0.1:8000/auth/register", { params: params })
		console.log(response);

		return response
	}
}