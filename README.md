## Domain-Gistry - A Domain Name Generation CLI


#### Part of DomainGistry Suite of Tools
+ DomainGistry Pkg
- Domain-Gisty CLI
- DomainGistry.js
- DomainGistry.jl


#### Requirements
+ Click
+ Click-did-you-mean


#### Installation
#### Method 1

+ Using Pip
```bash
tall domain-gistry
```


#### Method 2
+ Download repository on github
+ Change into directory
+ Type the following to install
```bash
tall -e .
```

### Usage

#### Global Usage
```bash
domain-gistry --help
```

#### Local Usage If You Used Repository
```bash
python domain-gistry.py --help
```


#### Generating Domain Names
+ Generate the domain name, shows you the common domain name generated, saves to a json file
```bash
domain-gistry.py generate yourdomainname
```
or

```bash
domain-gistry.py generate "yourdomainname"
```

+ Generate the domain name by category and with the option to save
```bash
 domain-gistry.py generate yourdomainname --category common --save yes
```
or

```bash
domain-gistry.py generate "yourdomainname" --category common --save yes
```

##### Screenshot
![](images/image.png)

#### Generating Domain Names By Category 
+ [Common | Extra | New | Prefixed | Suffixed]
+ Generate the domain name per category and show it on the console

#### Get Common Domain Names[.com,.org]
```bash
domain-gistry.py get-common "yourdomain name"

```
#### Get New Domain Names[.ai,.io]
```bash
domain-gistry.py get-new "yourdomain name"

```

#### Get Extra Domain Names[.tv,.media]
```bash
domain-gistry.py get-extra "yourdomain name"

```
#### Get Prefixed Domain Names[myexample.com,theexample.com]
```bash
domain-gistry.py get-prefix "yourdomain name"

```

#### Get Suffixed Domain Names[exampleworld.com,examplify.com]
```bash
domain-gistry.py get-suffix "yourdomain name"

```

#### Get All Domain Names
```bash
domain-gistry.py get-all "yourdomain name"

```



#### Author
+ Jesse E.Agbe(JCharis)
+ Jesus Saves@JCharisTech