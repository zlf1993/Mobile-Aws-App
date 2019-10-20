package com.longfei.zeng2017.ui.controller;

import com.fasterxml.jackson.databind.util.BeanUtil;
import com.longfei.zeng2017.service.UserService;
import com.longfei.zeng2017.shared.dto.UserDto;
import com.longfei.zeng2017.ui.model.request.UserDetailsRequestModel;
import com.longfei.zeng2017.ui.model.response.UserRest;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("users")
public class UserController {

    @Autowired
    UserService userService;

    @GetMapping(path="/{id}")
    public UserRest getUser(@PathVariable String id){

        UserRest returnValue = new UserRest();

        UserDto userDto = userService.getUserByUserId(id);
        BeanUtils.copyProperties(userDto, returnValue);

        return returnValue;
    }

    @PostMapping
    public UserRest createUser(@RequestBody UserDetailsRequestModel userDetails){
        UserRest returnValue = new UserRest(); // response return object
        UserDto userDto = new UserDto();
        BeanUtils.copyProperties(userDetails, userDto); // request data project to userDto

        UserDto createdUser = userService.createUser(userDto);

        BeanUtils.copyProperties(createdUser, returnValue);

        return returnValue;
    }

    @PutMapping
    public String updateUser(){
        return  "update user was called";
    }

    @DeleteMapping
    public String deleteUser(){
        return "delete user was called";
    }
}
