import requests

url = "https://edwardtanguay.vercel.app/share/skills.json"

response = requests.get(url)

if response.status_code == 200:
	data = response.json()

	for item in data[:5]:
		print(item)
else:
	print(f"Failed to fetch data: {response.status_code}")

