package com.longfei.zeng2017.exceptions;

import java.io.Serializable;

public class UserServiceException extends RuntimeException {


    private static final long serialVersionUID = -6614028180226880002L;

    public UserServiceException (String message) {
        super(message);
    }
}
