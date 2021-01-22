package com.example.demo.api;

//디펜던시 오류로 주석처리
// import com.example.demo.service.FlaskApiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

/*
    성진님이 알려주신 resttemplate 방법을 보기 이전에 코드를 작성했던 부분입니다.
    api 패키지의 FlaskApiController, RestApiController  를 추가했습니다.
    service 패키지의 FlaskApiService 를 추가했습니다.
*/

@Controller
public class  FlaskApiController {

    // 기본적인 동작방식은 index.html 을 렌더링 할 때 해당 문서 내부의 action에서 ec2플라스크 서버에 post리퀘스트를 하도록 요청하는 방식으로 작동
    // 스프링 서버에서 단순하게 html파일을 렌더링하고, flask api를 호출만 해주는 식으로 동작
    @GetMapping("/toFlask")
    public String FileUploads() {
        return "index"; // templates내부에 존재하는 html파일을 렌더링하지 못해 기본값을 넣어둠
    }
}

/*
 * 해당 코드를 짤 때 참조했던 링크입니다.
 * https://choichumji.tistory.com/39?category=849032
 * */

 /*
    final FlaskApiService flaskApiService;

    @Autowired
    public FlaskApiController(FlaskApiService flaskApiService){
        this.flaskApiService = flaskApiService;
    }



    // 플라스크 api에서 return하는 json데이터를 해당 변수에 넣어야하는 issue 가 있음\
    @GetMapping("/apiToFlask")
    public String getJson(){
        Model model = null;
        String responce = flaskApiService.getJsonData();
        model.addAttribute("responce", responce);
        // 정상적으로 동작하는지 test하는 코드, 확인이후 지울것
        System.out.println("사용자가 넣은 사진의 label = " + responce);
        return responce;
    }

}
*/