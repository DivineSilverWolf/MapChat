package org.example.dao;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.sql.Time;
import java.util.Date;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Message {
    @Id
    @GeneratedValue(strategy =  GenerationType.AUTO)
    Long id;

    @ManyToOne
    User user;

    String messageText;
    Date timestamp;

    public Message(User user, String messageText, Date timestamp) {
        this.user = user;
        this.timestamp = timestamp;
        this.messageText = messageText;
    }
}
