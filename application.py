from sys            import argv
from flask          import Flask, render_template
from flask.ext.mail import Message, Mail
from flask.ext.wtf  import Form, TextField, Required, RecaptchaField


application = Flask(__name__)
application.config.update(
    MAIL_SERVER   = 'smtp.gmail.com',
    MAIL_PORT     = 465,
    MAIL_USE_SSL  = True,
    MAIL_USE_TLS  = False,
    MAIL_USERNAME = 'consult.karen.site.mailer',
    MAIL_PASSWORD = 'T5zclrIRkOs2',

    CSRF_ENABLED = True,
    SECRET_KEY   = 'afs;345;elfja',

    RECAPTCHA_PUBLIC_KEY  = '6Le-9N8SAAAAAD5hV6U8K7KMMBDwV78djjb8N3hy',
    RECAPTCHA_PRIVATE_KEY = '6Le-9N8SAAAAAF4PlN307oUrXE6diQnxXee0rGqL',
    RECAPTCHA_USE_SSL     = True
)

mailer = Mail(application)


@application.route("/")
@application.route("/blog/")
def blog():
    return render_template('blog.html')


@application.route("/about/")
def about():
    return render_template('about.html')


@application.route("/contact/", methods=['POST', 'GET'])
def contact():
    contact_form = ContactForm()

    if contact_form.validate_on_submit():

        message = Message("New email from your website!",
                          sender="consult.karen.site.mailer@gmail.com",
                          recipients=["kprice@tiac.net"])

        message.body = "SENDER:\n" + contact_form.name.data + "\n\n" + \
                       "SENDER EMAIL:\n" + contact_form.email.data + "\n\n" + \
                       "MESSAGE:\n" + contact_form.message.data

        mailer.send(message)

        return render_template('thanks.html', name=contact_form.name.data)

    return render_template('contact.html',
                           form=contact_form)


@application.route("/projects/")
def projects():
    return render_template('projects.html')


@application.route("/consulting/")
def consulting():
    return render_template('consulting.html')


@application.route("/publications/")
def publications():
    return render_template("publications.html")


@application.route("/advisory_boards/")
def advisory_boards():
    return render_template("advisory_boards.html")


@application.route("/conference_papers/")
def conference_papers():
    return render_template("conference_papers.html")


@application.route("/keynotes_and_plenaries/")
def keynotes_and_plenaries():
    return render_template("keynotes_and_plenaries.html")


@application.route("/teaching_and_workshops/")
def teaching_and_workshops():
    return render_template("teaching_and_workshops.html")


class ContactForm(Form):
    name      = TextField     ('name' ,   validators=[Required()])
    email     = TextField     ('email',   validators=[Required()])
    message   = TextField     ('message', validators=[Required()])
    recaptcha = RecaptchaField()


if __name__ == '__main__':
    debug = True if len(argv) == 2 and argv[1] == 'debug' else False
    if debug:
        application.run(debug=True, host='0.0.0.0', port=8000)
    else:
        application.run(debug=False, host='0.0.0.0')
