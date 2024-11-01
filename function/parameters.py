# default parameter
def default_parameter(name='Python'):
    print(f'{name}')

default_parameter()
default_parameter('JavaScript')

# keyword arguments
def keyword_arguments(language, framework):
    print(f'{language} {framework}')

keyword_arguments('Python', 'Django')
keyword_arguments(framework='Django', language='Python')

# *args parameters
def args_parameter(*args):
    print(f'{args}')

args_parameter('Python')
args_parameter('Python', 'JavaScript')

# **kwargs parameters
def kwargs_parameter(**kwargs):
    print(f'{kwargs}')

kwargs_parameter(language='Python')
kwargs_parameter(language='Python', framework='Django')