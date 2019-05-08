from flask import Flask, render_template, request

app = Flask(__name__, static_url_path = "", static_folder = "templates")

original_questions = {
	#Format is 'question':[options]
	'What is a computer network?':[
		'A super computer owned only by the government',
		'A web of connected computers or devices',
		'A computer vulnerability',
		'An internet service provider'
	],
	'Which of these groups exploits cyber vulnerabilities?':[
		'Criminals',
		'Government',
		'Hacktivists',
		'All of these'
	],
	'According to secret lives of hacker, what is hacking?':[
		'Problem solving by using an objects properties in unexpected way',
		'Creating problems where there previously were none',
		'Using materials as they were intended to be used to solve problems',
		'All of the above'
	],
	'Which of these is not a hack?':[
		'Using a bicycle to power a computer',
		'Stealing an unlocked bicycle',
		'Building a working bicycle out of discarded umbrellas',
		'Creating a kinetic bicycle sculpture'
	],
	'Which of the following may intercept and use your messages for their own purposes?':[
		'News outlets',
		'Governments',
		'Advertising agencies',
		'Crime rings', 
		'All of the above'
	]
}

answers_map = {
	'What is a computer network?': 'A web of connected computers or devices',
	'Which of these groups exploits cyber vulnerabilities?': 'All of these',
	'According to secret lives of hacker, what is hacking?': 'Problem solving by using an objects properties in unexpected way',
	'Which of these is not a hack?': 'Stealing an unlocked bicycle',
	'Which of the following may intercept and use your messages for their own purposes?': 'All of the above'
}

@app.route('/')
def quiz():
	questions = original_questions.keys()
	return render_template('main.html', q = questions, o = original_questions)

@app.route('/quiz', methods=['POST'])
def quiz_answers():
	score = 0
	response = request.form.to_dict()
	for key in response.keys():
		check_key = str(key).strip()
		if response[key] == answers_map[check_key]:
			score = score + 1

	return '<h1>Your Score is: <u>' + str(score) + '</u></h1>'

if __name__ == '__main__':
	app.run(debug=True)