# .gitignore - Modèle complet (multi-stack)

> Objectif : un `.gitignore` **prêt à l'emploi** pour la plupart des projets (Node.js, Python, Java/C#, mobile, web). Inclut les fichiers système (par exemple `.DS_Store`) et les fichiers indésirables de l'IDE. Adaptez-vous si nécessaire - en particulier dans les **lockfiles** et **.vscode**.

## Comment utiliser

1. Copiez le bloc ci-dessous dans un fichier appelé `.gitignore` à la racine du référentiel.
2. Passez en revue les sections **commentées** (fichiers de verrouillage, .vscode) et ajustez-les à votre contexte.
3. Pour les monorepos, conservez ce `.gitignore` à la racine ; les sous-dossiers peuvent avoir leur propre `.gitignore` supplémentaire.

> Remarque sur les **fichiers de verrouillage** (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `Pipfile.lock`, `poetry.lock`) : **en règle générale, vous devez COMMIT** le fichier de verrouillage dans les applications ; **ne** l'ignorez pas à moins que vous sachiez pourquoi. Je laisse les lignes commentées pour éviter de les ignorer par erreur.

---

## Template (complete .gitignore)

```gitignore
###############################
# SISTEMA / OS                #
###############################

# macOS
.DS_Store
.DS_Store?
.AppleDouble
.LSOverride
Icon
Icon?
._*
.Spotlight-V100
.Trashes
.fseventsd

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/
*.lnk

# Linux
*~
.nfs*

# Comum
*.stackdump

###############################
# EDITORES / IDEs             #
###############################

# VS Code (ignora tudo por defeito, mas permite partilhar 2 ficheiros úteis)
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json

# JetBrains (IntelliJ/IDEA, PyCharm, Rider, etc.)
.idea/
*.iml

# Sublime / Vim / Emacs
*.sublime-workspace
*.sublime-project
*.swp
*.swo
*~
.emacs.d/

# Xcode
*.xcworkspace/
*.xcuserstate
*.xcuserdatad/
*.xccheckout
*.xcodeproj/project.xcworkspace/
*.xcodeproj/xcuserdata/
*.xcscmblueprint
DerivedData/

###############################
# AMBIENTES / SEGREDOS        #
###############################

.env
.env.*
.envrc
.venv/
venv/
venv*/
**/.env
**/.env.*
*.key
*.pem
*.p12
*.crt
*.cer
*.der
*.jks
*.keystore
*.pfx
*.secret
secrets.*
secret.*
*.token

###############################
# NODE / JS / TS              #
###############################

# Dependências e artefactos
node_modules/
**/node_modules/
bower_components/
jspm_packages/
.npm/
.pnpm-store/
.yarn/
.yarn/cache/
.yarn/unplugged/
.yarn/build-state.yml
.yarn/install-state.gz

# Logs e caches
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*
*.log
.eslintcache
.stylelintcache
.cache/
.cache-loader/
.parcel-cache/
.vite/
.next/
.nuxt/
.svelte-kit/
.storybook-out/
storybook-static/

# Builds
dist/
build/
out/

# TypeScript
*.tsbuildinfo

# Lockfiles (normalmente deves COMMITAR - mantém comentado a menos que decidas ignorar)
# package-lock.json
# yarn.lock
# pnpm-lock.yaml

###############################
# FRONTEND / WEB              #
###############################

# Frameworks/Tools
.tmp/
.tmp/*
.sass-cache/
bower_components/
coverage/
.nyc_output/

# Static hosts
.vercel/
.netlify/

###############################
# PYTHON                      #
###############################

# Compilados / cache
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so
*.dylib

# Builds / dist
build/
dist/
wheels/
*.egg-info/
.eggs/
*.egg
develop-eggs/
.installed.cfg
pip-wheel-metadata/

# Testes / ferramentas
.coverage
.coverage.*
htmlcov/
.tox/
.nox/
.pytest_cache/
.cache
.pyre/
.mypy_cache/
.pytype/
.ipynb_checkpoints/

# Ambientes virtuais (ver também secção AMBIENTES)
venv/
.venv/
env/
env*/

# Lockfiles (em geral, COMMITAR)
# Pipfile.lock
# poetry.lock
# requirements.lock

###############################
# JAVA / JVM                  #
###############################

# Gradle / Maven
.gradle/
build/
target/
out/
**/build/
**/target/
.mvn/wrapper/maven-wrapper.jar
!/.mvn/wrapper/maven-wrapper.jar

# IDE metadata
.settings/
.project
.classpath

# Bytecode / dumps
*.class
hs_err_pid*
replay_pid*

###############################
# C / C++ / GCC / CLANG       #
###############################

*.o
*.obj
*.gch
*.pch
*.a
*.lib
*.dll
*.so
*.dylib
*.exe
*.out
*.app

###############################
# C# / .NET                   #
###############################

# Artefactos
[Bb]in/
[Oo]bj/
[Ll]og/
[Tt]est[Rr]esult*/

# IDE / misc
.vs/
*.user
*.suo
*.userprefs
*.csproj.user
*.rsuser

# NuGet
*.nupkg
*.snupkg
packages/
# project.lock.json (obsoleto, não usar)
project.lock.json

###############################
# GO                          #
###############################

bin/
pkg/
*.test

###############################
# RUBY                        #
###############################

.bundle/
vendor/bundle/
coverage/
tmp/
log/
*.gem

###############################
# PHP / COMPOSER              #
###############################

vendor/
# composer.lock (em apps normalmente COMMITAR)
# composer.lock

###############################
# ANDROID                     #
###############################

.gradle/
/local.properties
.cxx/
captures/
*.apk
*.aab

###############################
# iOS / COCOA                 #
###############################

Pods/
Carthage/
fastlane/report.xml
fastlane/Preview.html
fastlane/screenshots
fastlane/test_output

###############################
# DOCKER                      #
###############################

.docker/
docker-compose.override.yml

###############################
# BASES DE DADOS / DATA       #
###############################

*.sqlite
*.sqlite3
*.db
*.mdb
*.tgz
*.tar
*.tar.gz
*.gz
*.7z
*.zip
*.rar
*.bak
*.old
*.orig
*.tmp

###############################
# DOCUMENTAÇÃO / OFFICE       #
###############################

~$*.doc*
~$*.xls*
~$*.ppt*

###############################
# MISC                        #
###############################

# Relatórios / cobertura
coverage/
reports/

# Artefactos diversos
Thumbs.db
Desktop.ini
.DS_Store
```

---

## Derniers conseils

- Garde `.gitignore` **court et vérifiable** ; supprime ce qui n'a pas de sens pour le projet.
- Préférable **commit lockfiles** (Node, Python, PHP) dans les applications pour des builds reproductibles.
- En monorepos, `.gitignore` à la racine + ajustements granulaires à chaque package si nécessaire.
