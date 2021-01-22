# FooDetector Project Client Part Repository

![GitHub
License](https://img.shields.io/github/license/Silicon-Valley-Online-Internship/Client-Spring-React)
![GitHub repo size](https://img.shields.io/github/repo-size/Silicon-Valley-Online-Internship/Client-Spring-React)
![GitHub
contributors](https://img.shields.io/github/contributors/Silicon-Valley-Online-Internship/Client-Spring-React)
![GitHub
stars](https://img.shields.io/github/stars/Silicon-Valley-Online-Internship/Client-Spring-React?style=social)
![GitHub
forks](https://img.shields.io/github/forks/Silicon-Valley-Online-Internship/Client-Spring-React?style=social)
![GitHub
issues](https://img.shields.io/github/issues/Silicon-Valley-Online-Internship/Client-Spring-React?style=social)

팀 CoCo(Corona Coder)의 **FooDetector** 를 소개합니다.</br>
Introducing CoCo(Corona Coder) Team's **FooDetector**</br>

이 프로젝트는 **사진 내의 음식을 인식하고** 학습된 데이터를 기반하여 편리한 기능을 지원하는 웹기반 프로젝트입니다.<br/> 
This project is a web-based project that supports a function that **recognizes food in pictures**.<br/> 

## How to install
```> git clone https://github.com/Silicon-Valley-Online-Internship/Client-Spring-React.git```
</br>intellij 에서 프로젝트 run

## How did we link React and SpringBoot?
1. IntelliJ 에서 제공해주는 Spring initializar를 통해 Spring Boot 프로젝트 생성 (type : Gradle, dependency : Spring Web )</br></br>
2. SpringProjectName\src\main\ 경로에 React 프로젝트 파일 추가 ( 아직 react 파일이 없다면  ```create-react-app```를 통해 설치해 줄 수 있다.)</br></br>
3. 설치가 완료 후 설치한 파일로 경로 이동
``` 
> cd [react Project name] 
> npm start 
```
4. 정상적으로 잘 작동된다면 ```npm install```을 실행</br></br>
5. ```npm run-script build``` 명령어를 실행 compiled successfully라고 뜨면 제대로 빌드된 것이다.</br></br>
6. npm run eject를 실행시킨다. -> 만약 에러가 난다면 Git에 전부 데이터를 Push 하고 다시 시도한다.</br></br>
7. 새로 생성된 [react Project name]/config/paths.js에 가서 appBuild: resolveApp('build')에 /static을 추가해준다.</br>
```
appBuild: resolveApp('build') -> appBuild: resolveApp('build/static')
```
8. 이후 [react Project name]/build로 가서 모든 파일을 삭제한다.</br></br>
9. spring의 build.gradle파일에서 react와 spring이 같이 빌드될 수 있도록 정의해준다.(코드 참고)</br></br>
10. build & run 했을때 아래와 같은 결과가 나오면 </br></br>
![image](https://user-images.githubusercontent.com/55476465/104579819-d2b81400-569f-11eb-8057-5f0912b37c37.png)</br>
localhost:8080에서 react화면이 호출되는 것을 확인할 수 있습니다.</br>
<hr>

### TODO
 - 화면 설계
 - API 연동
 - Docker
 - TDD 설계

<hr>

## Member

Front : </br>
류서현 <ryuish541@gmail.com></br>
박찬 <dkssudgkdl9@naver.com></br>

Back : </br>
최용석 <dydtjr1717@gmail.com></br>
안성진 <seongjin.dev@gmail.com></br>
