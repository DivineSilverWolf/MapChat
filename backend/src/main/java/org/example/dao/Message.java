package org.example.dao;

import jakarta.persistence.*;

import java.sql.Time;
import java.util.Optional;

@Entity
public class Message {
    @Id
    @GeneratedValue(strategy =  GenerationType.AUTO)
    Long id;
    @ManyToOne
    User user;
    String messageText;
    Time timestamp;

    public Message(User user, String messageText, Time timestamp) {
        this.user = user;
        this.timestamp = timestamp;
        this.messageText = messageText;
    }
}
