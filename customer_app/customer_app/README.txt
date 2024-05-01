
(OVERVIEW)

I have made a VERY simple django project called customer_app, with a single app inside of it called customer_app. You can launch the project by going to the project home directory (after installing the very few requirements listed in requirements.txt located above the root project directory by running pip -m requirements.txt) you can run:

>> python manage.py runserver 

Navigate to 127.0.0.1:8000/customers/

and you will see some test data that I put in, along with a button to fill in information for new customers.



1. ADD UNIT TESTS

In the interest of brevity, I have included a feature for restricting the FirstName field on the Customer model. This is meant to mimic other application functionality that will enforce uniformity in data input to the database. If you attempt to submit a customer with an empty "First Name" field the webpage with give you a polite pop up to please fill the field in. 

Consequently, I have also provided a /tests module within customer_app that contains a TestCase class for testing this specific functionality. The TestCustomerForm class inherits from the TestCase base class and all test cases declared inside of it can be run from the project root directory with this command:

>>DJANGO_SETTINGS_MODULE=customer_app.settings pytest ./customer_app/customer_app/tests/tests.py::TestCustomerForm


2. PROVE YOUR CODE IS HIGH QUALITY

It is difficut to "prove" that any given code project is high quality objectively. As project needs change one might find themselves completely reconfiguring resources, settings, applications within a project to suit thier needs. Therefore - a "good" design decision can very easily turn into a headache down the road making the proving of such a thing difficult.

I can however, make a convincing argument that my project sticks fairly close to the suggested usage of a django application/module framework. Django provides an excellent bedrock from which you can build all sorts of well designed functionality and tests therein. I have created a subfolder in my customer_app module called /tests - the file within "tests.py" has a single TestCase class that can have additional tests added to it to cover more processes as they are developed and a similiar methodology can be used to provide code coverage for other adjacent apps as well making the class easily scalable to other applications if needed while keeping each suite of tests seperated by functionality as you continute to define it. The Customer model is very plain with arbitrary constraints placed on the columns for mostly illustrative purposes. There are two views that sit neatly on top of the django ORM for query management. 

3. What would you do to ensure that expansion of the test app maintains good code quality

Linters like "black" and unit testing plugins associated with pre-commit hooks are a good tool to put into common practice amongst development teams are a good idea to make sure everyones usage of different code elements is similiar and to maximize readibility. The only way to ensure that code quality is maintained in the end is in the review process and to ensure that developers communicate and author code in a unified way. There is MUCH more to maintaining code quality than any tool or subset of tools can provide. Just like there is no algorithm for truth, there is no single thing better than good communication to keep the chaos at bay.