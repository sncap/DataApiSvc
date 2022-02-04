package com.cds.api.entity;

import org.hibernate.validator.constraints.CreditCardNumber;

import javax.validation.constraints.*;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name="person")
@XmlAccessorType(XmlAccessType.FIELD)
public class Person {
    private long id;
    private String firstName;

    @NotNull
    @NotBlank
    private String lastName;

    // 정규식으로 이메일의 유효성을 판단한다.
    @Pattern(regexp = ".+@.+\\..+", message = "Please provide a valid email address")
    private String email;

    // @Email annotation 으로 이메일의 유효성을 판단한다.
    @Email()
    private String email1;

    // @Min, @Max annotation 으로 최소, 최대값을 지정한다.
    @Min(18)
    @Max(30)
    private int age;

    // 신용카드번호의 유효성을 판단한다.
    @CreditCardNumber
    private String creditCardNumber;

    public String getCreditCardNumber(){
        return creditCardNumber;
    }

    public void setCreditCardNumber(String creditCardNumber){
        this.creditCardNumber = creditCardNumber;
    }

    public long getId(){
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }
    public String getEmail1() {
        return email1;
    }
    public void setEmail1(String email1) {
        this.email1 = email1;
    }

    @Size(min = 2)
    public String getFirstName(){
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
    public String getLastName() {
        return lastName;
    }
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
}
