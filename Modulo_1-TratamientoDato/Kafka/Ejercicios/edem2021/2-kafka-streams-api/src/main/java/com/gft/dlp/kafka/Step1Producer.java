package com.gft.dlp.kafka;

import com.github.javafaker.Faker;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;
import java.util.concurrent.TimeUnit;

public class Step1Producer {

    public static final String INPUT_TOPIC = "quotes-input";

    public static void main(String[] args){
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        KafkaProducer<String, String> kafkaProducer = new KafkaProducer<String, String>(properties);
        Faker faker = new Faker();
        try{
            for(int i = 0; i < 1000; i++){
                String quote = faker.shakespeare().asYouLikeItQuote();
                System.out.println(quote);
                kafkaProducer.send(new ProducerRecord<String, String>(INPUT_TOPIC, quote ));
            }
            while(true){
                //Duplicated code only for didactic purpouses
                String quote = faker.shakespeare().asYouLikeItQuote();
                System.out.println("Send to the Kafka topic " + INPUT_TOPIC + " the randomly generated " +
                        "shakespeare quote ["+ quote+"]");
                kafkaProducer.send(new ProducerRecord<String, String>(INPUT_TOPIC, quote ));
                // delay 5 seconds
                TimeUnit.SECONDS.sleep(5);
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            kafkaProducer.close();
        }
    }
}