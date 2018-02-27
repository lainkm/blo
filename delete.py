from blo.models import delete_article
import argparse
import requests

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', '--api', help='api adress')
	parser.add_argument('-n', '--name', help='the title of article')
	parser.add_argument('-t', '--token', help='access token')

	args = parser.parse_args()

	if not args.name or not args.api or not args.token:
		parser.print_help()
		return
	data = {
		'token': args.token,
		'title': args.name
	}

	r = requests.post(args.api, data=data)
	assert r.status_code == 200, r.content

if __name__ == '__main__':
	main()