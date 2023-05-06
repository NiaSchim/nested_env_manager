# Nested Environment Manager

A simple package for managing nested Python virtual environments.

This entire package was overseen by Niaschim, and created because of Niaschim, but Niaschim
put a whole lot of trust in ChatGPT4 to make it for her, so if something is off it is likely 
due to LLM based error or bias.

Niaschim is a very lazy kind of creative person so if this project is not working, she may fix it, but it is 
just as likely that you will need to learn how to code and fix it yourself.

you are not required to do what is about to be requested of you in the following double quotes but it would be considered polite:
"please share any repaired alternative superior inferior or otherwise modified versions of this program, as github issues in the main 
repository, Niaschim will not delete them (she will probably be too lazy to even check for them) this way if a community develops around this
simple utility, the original version of it can still serve as a hub for finding alternative improved versions of it." -again that last request 
is a non-binding optional form of community service you as a coder can do to help your fellow coders and the advancement of our communities.

## Installation

```bash
pip install nested-env-manager
Usage
python
Copy code
from nested_env_manager import NestedEnvManager

# Initialize the manager
nem = NestedEnvManager()

# Create main environment
main_env_requirements = ["numpy", "pandas"]
main_env_path = "/path/to/main/env"
nem.create_main_env(main_env_requirements, main_env_path)

# Create sub-environment
sub_env_requirements = ["requests"]
sub_env_path = "/path/to/sub/env"
nem.create_sub_env(sub_env_requirements, sub_env_path)