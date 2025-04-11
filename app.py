from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    subject = request.form.get('subject')
    other_subject = request.form.get('other_subject')
    contact_method = request.form.getlist('contact_method')
    agreement = request.form.get('agreement')

    errors = []

    if not all([name, email, phone, message, subject, agreement]):
        errors.append("All fields except 'Other Subject' must be filled.")
    if not phone.isdigit():
        errors.append("Phone number must be numeric.")
    if subject == 'Other' and not other_subject:
        errors.append("Please specify the subject.")

    if errors:
        return render_template('contact_form.html', errors=errors)

    if subject == "Other":
        final_subject = other_subject
    else:
        final_subject = subject

    return render_template('confirmation.html', name=name, email=email, phone=phone,
                           message=message, subject=final_subject,
                           contact_method=', '.join(contact_method), agreement='Yes')

if __name__ == '__main__':
    app.run(debug=True)