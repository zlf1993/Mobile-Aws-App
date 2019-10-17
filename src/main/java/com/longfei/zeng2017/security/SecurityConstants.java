package com.longfei.zeng2017.security;

import com.longfei.zeng2017.SpringApplicationContext;

public class SecurityConstants {
    public static final long EXPIRATION_TIME = 86400000; //1 day
    public static final String TOKEN_PREFIX = "Bearer";
    public static final String HEADER_STRING = "Authorization";
    public static final String SIGN_UP_URL = "/users";
    //public static final String TOKEN_SECRET = "jf9i4jgu83nfl0";
     public static String getTokenSecret() {
        AppProperties appProperties = (AppProperties) SpringApplicationContext.getBean("appProperties");
        return appProperties.getTokenSecret();

     }

}
