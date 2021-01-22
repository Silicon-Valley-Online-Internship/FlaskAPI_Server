
// 디펜던시 오류로 코드 전체 주석처리

/*package com.example.demo.service;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.config.EnableWebFlux;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.spring.context.config.EnableReactor;

@EnableReactor
@EnableWebFlux
@Service
public class FlaskApiService {

    private final WebClient webClient;

    @Autowired
    public  FlaskApiService(WebClient.Builder webClientBuiler){
        this.webClient = webClientBuiler.baseUrl("http://18.217.223.132:5000/upload").build();
    } // flask server의 파일 업로드 주소를 기본으로 설정


    // 이게 맞을까...?
    public String getJsonData(){
        String response =
                this.webClient.get().uri("/fileUpload")
                .retrieve().bodyToMono(String.class)
                .block();
        return response;
    }

}
*/