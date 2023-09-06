build:
	docker build -t calendar .

run: build
	docker run \
	  -v ./data:/data \
		-v ./img:/img \
		--rm \
		--name calendar \
		calendar

clean:
	docker stop calendar
	docker rm calendar
