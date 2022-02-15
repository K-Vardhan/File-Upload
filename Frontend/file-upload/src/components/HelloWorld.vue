<template>
<div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">File Uploader</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Upload</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Pdf List</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <section class="container-fluid">
        <section class="row justify-content-center">
            <section class="col-12 col-sm-6 col-md-3">
                <form class="form-container">
                    <div class="mb-3">
                        <label class="form-label">File Name</label>
                        <input type="text" v-model="name" class="form-control" />
                    </div>
                    <div class="mb-3">
                        <label for="formFile" class="form-label">Select PDF file</label>
                        <input class="form-control" @change="handleFileUpload( $event )" type="file" />
                    </div>

                    <div class="d-grid gap-2">
                        <button v-on:click="submitFile()" class="btn btn-dark" type="button">
                            Submit
                        </button>
                    </div>
                </form>
            </section>
        </section>
    </section>


    
</div>
</template>

<script>
import axios from "axios";

export default {
    name: "App",
    data() {
        return {
            name: '',
            pdf_file: '',
        };
    },
    methods: {
        handleFileUpload(event) {
            this.pdf_file = event.target.files[0];
        },
        submitFile() {
            let formData = new FormData();
            formData.append("name", this.name);
            formData.append("pdf_file", this.pdf_file);
            axios
                .post("http://localhost/api/FileUploade/", formData)
                .then(function (res) {
                    console.log(res);
                });
        },
    },
};
</script>

<style scoped>
.form-container {
    position: absolute;
    top: 20vh;
    background: #fff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 0px #000;
}
</style>
