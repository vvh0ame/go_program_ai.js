from requests import get

class GoProgramAI:
	def __init__(self) -> None:
		self.api = "https://api.goprogram.ai"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_inspiration(self) -> dict:
		return get(
			f"{self.api}/inspiration", headers=self.headers).json()
