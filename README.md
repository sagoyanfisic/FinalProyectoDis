<h1>Proyecto de Diseño de sistemas</h1> <br>

<font> Manual para la instalación de Framework Django</font> <br>

<font>Python tools</font><br>
<code>sudo apt-get install python-setuptools </code> <br>
<code> sudo apt-get install python-django</code><br>
<font>Inciar proyecto</font> <br>
<code> $ mkdir hellodjango && cd hellodjango </code>
  <code> django-admin startproject nombreProyecto </code><br>
<code> cd nombreProyecto/ </code><br>
<code> python manage.py runserver </code><br>
<code>python manage.py syncdb </code><br>

<storge>Uso de South para hacer cambios en la BD y no perder datos en transcurso:</storge><br>
http://south.aeracode.org/<br>
<storge>Documentación de South:</storge><br>
http://south.readthedocs.org/en/latest/<br>

Iniciando la migración con south : <br>
<code>$ python manage.py schemamigration principal --initial</code> <br>
<code>$ python manage.py migrate principal </code>

Test de aplicacion 
-----------------------------

1. Test para levantar servicio de Django en el sevidor::

	<pre>$ python hellodjango/manage.py runserver
	Validating models...
	0 errors found
	Django version 1.3, using settings 'hellodjango.settings'
	Development server is running at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.
	Ctrl-C to exit the server.</pre>

Deploy de aplicaciòn de Heroku
------------------------------------

1. Modificar   ::

 Agregar al fichero  .gitignore ::
<pre>
	bin
	build
	include
	lib
	.Python
	*.pyc
</pre>
2. Inicializar el proyecto ::

<pre>
	$ git init
	Initialized empty Git repository in /Users/adam/hellodjango/.git/
	$ git add .
	$ git commit -m "my django app"
	[master (root-commit) 8c07531] my django app
	5 files changed, 184 insertions(+), 0 deletions(-)
	create mode 100644 .gitignore
	create mode 100644 hellodjango/__init__.py
	create mode 100644 hellodjango/manage.py
	create mode 100644 hellodjango/settings.py
	create mode 100644 hellodjango/urls.py
	create mode 100644 requirements.txt
	Deploy to Heroku
</pre>

3. Crear aplicación previo logeo ::

<pre>
	$ heroku create --stack "aplicacion"
	Creating afternoon-sword-29... done, stack is cedar
	http://afternoon-sword-29.herokuapp.com/ | git@heroku.com:afternoon-sword-29.git
	Git remote heroku added
</pre>

4. Deploy la app::

<pre>
	$ git push heroku master
	Counting objects: 9, done.
	Delta compression using up to 4 threads.
	Compressing objects: 100% (6/6), done.
	Writing objects: 100% (9/9), 3.01 KiB, done.
	Total 9 (delta 0), reused 0 (delta 0)

	-----> Heroku receiving push
	-----> Python/Django app detected
	-----> Preparing virtualenv version 1.6.1
		New python executable in ./bin/python2.7
		Also creating executable in ./bin/python
		Installing setuptools............done.
		Installing pip...............done.
	-----> Byte-compiling code
	-----> Django settings injection
		Injecting code into hellodjango/settings.py to read from DATABASE_URL
	-----> Installing dependencies using pip version 1.0.1
	Downloading/unpacking Django==1.3 (from -r requirements.txt (line 1))
	...
		Successfully installed Django psycopg2
		Cleaning up...
	-----> Discovering process types
		Procfile declares types         -> (none)
		Default types for Python/Django ->web
	-----> Compiled slug size is 8.0MB
	-----> Launching... done, v3
		http://afternoon-sword-29.herokuapp.com deployed to Heroku

	To git@heroku.com:afternoon-sword-29.git
	* [new branch]      master -> master
</pre>

5. Checking de los procesos " ps"::

<pre>
	$ heroku ps
	Process       State               Command
	------------  ------------------  ------------------------------
	web.1         up for 4s           python hellodjango/manage.py r..
</pre>


6. Visualizar  logs::

<pre>
	$ heroku logs
	2011-08-27T07:58:00+00:00 heroku[web.1]: Starting process with command `python hellodjango/manage.py runserver 0.0.0.0:8642 --noreload`
	2011-08-27T07:58:00+00:00 app[web.1]: Validating models...
	2011-08-27T07:58:00+00:00 app[web.1]: 
	2011-08-27T07:58:00+00:00 app[web.1]: 0 errors found
	2011-08-27T07:58:00+00:00 app[web.1]: Django version 1.3, using settings 'hellodjango.settings'
	2011-08-27T07:58:00+00:00 app[web.1]: Development server is running at http://0.0.0.0:8642/
	2011-08-27T07:58:00+00:00 app[web.1]: Quit the server with CONTROL-C.
	2011-08-27T07:58:01+00:00 heroku[web.1]: State changed from starting to up
</pre>

7. Finalizar app , lvantar::

	<code>$ heroku open</code>
	

	
