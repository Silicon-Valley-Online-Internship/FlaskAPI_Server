package com.example.demo.api;


import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.HttpServerErrorException;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponents;
import org.springframework.web.util.UriComponentsBuilder;

import java.util.HashMap;
import java.util.Map;

//해당부분은 성진님이 알려주신 resttemplates를 검색하면서 짰던 코드입니다.
//FlaskApiController 와는 별개의 코드입니다.


@RestController
public class RestApiController {


    @GetMapping
    public String callApi() throws JsonProcessingException{

        HashMap<String , Object> result = new HashMap<String, Object>();

        String responce = "";

        try{

            HttpComponentsClientHttpRequestFactory factory = new HttpComponentsClientHttpRequestFactory();
            factory.setConnectTimeout(15000); //타임아웃 설정 15초
            factory.setReadTimeout(15000);//타임아웃 설정 15초
            RestTemplate restTemplate = new RestTemplate(factory);

            HttpHeaders header = new HttpHeaders();
            HttpEntity<?> entity = new HttpEntity<>(header);

            String url = "http://";
        }catch (HttpClientErrorException | HttpServerErrorException e){


        }
        return responce;
    }


}
